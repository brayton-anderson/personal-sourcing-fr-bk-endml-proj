import {
  GithubAuthProvider,
  GoogleAuthProvider,
  onAuthStateChanged,
  signInWithPopup,
  signOut,
  User,
} from 'firebase/auth'
import { useRouter } from 'next/router'
import { createContext, useContext, useEffect, useRef, useMemo, useState } from 'react'
import {UserData} from '../services/userData'
import authService from '../services/authService'
import Users from '../services/userService'
import  signupNotif from '../utils/utils'
import { async } from '@firebase/util'
import { auth } from '../../firebase'

interface IAuth {
  user: UserData | null
  users: User | null
  rems: number | null
  signUp: (username: string, email: string,  password: string, password2:string, agreement: boolean) => Promise<void>
  signIn: (username: string, _password: string, rem: boolean) => Promise<void>
  resetPass: (password: string, password2:string) => Promise<void>
  resetAuth: (email: string) => Promise<void>
  verifyCode: (code: string, email: string, page: string) => Promise<void>
  signWithGithub: () => Promise<void>
  signWithGoogle: () => Promise<void>
  logout: () => Promise<void>
  error: string | null
  loading: boolean
}

const AuthContext = createContext<IAuth>({
  user: null,
  users: null,
  rems: null,
  signUp: async () => {},
  signIn: async () => {},
  resetPass: async () => {},
  resetAuth: async () => {},
  verifyCode: async () => {},
  signWithGithub: async () => {},
  signWithGoogle: async () => {},
  logout: async () => {},
  error: null,
  loading: false,
})

interface AuthProviderProps {
  children: React.ReactNode
}

const provider = new GithubAuthProvider();
const prov = new GoogleAuthProvider();
provider.addScope('repo');
provider.setCustomParameters({
  'allow_signup': 'true'
});

export const AuthProvider = ({ children }: AuthProviderProps) => {
  const router = useRouter()
  const [user, setUser] = useState<UserData | null>(null)
  const [users, setUsers] = useState<User | null>(null)
  const [rems, setLoads] = useState<number | null>(null)
  const [error, setError] = useState(null)
  const [initialLoading, setInitialLoading] = useState(true)
  const [loading, setLoading] = useState(false)

  const requestRef = useRef<UserData | null>()
  
  useEffect(
    () =>{
     const handleResiz = async() => {
      let data = await Users.getUserData("user")
      if (data != null) {
        requestRef.current = data['user']
        // Logged in...
        setUser(requestRef.current!)
        setLoading(false)
      } else {
        onAuthStateChanged(auth, (users) => {
        if (users) {
          // Logged in social...
          setUsers(users)
          setLoading(false)
        } else {
          // Not logged in...
          setUser(null)
          setLoading(true)
          if(rems == null){
          router.push('/login')
          setLoads(1)
        }
        }

        setInitialLoading(false)
      })
      }
    }
      handleResiz()
      setInitialLoading(false)
    }, [rems, router, user]
  )

  const signIn = async (username: string, _password: string, rem: boolean) => {
    setLoading(true)

      if (_password.length <= 8) signupNotif("passwords must be atleast 9 characters", "1", "pass")
      else if (username.length <= 5) signupNotif("Email must be atleat 6 characters", "1", "mail")
      else{
        await authService.signIn(username, _password).then((res) => {
          let new2 = res['data']
         if(new2 == "wrong username") signupNotif(new2, "1", "mail")
         else if(new2 == "wrong password" ) signupNotif(new2, "1", "pass")
         else {
          localStorage.setItem("user", JSON.stringify(new2))
          setUser(new2)
          router.push('/')
          setLoading(false)
         } 
        }).catch((error) => signupNotif(error.message, "3", "mail"))
        .finally(() => setLoading(false)) 
      }
  }

  const signUp = async (username: string, email: string,  password: string, password2:string, agreement: boolean) => {
    setLoading(true)
    if(password != password2) signupNotif("passwords do not match", "2", "pass")
    else if (password.length <= 8) signupNotif("passwords must be atleast 9 characters", "1", "pass")
    else if (email.length <= 5) signupNotif("Email must be atleat 6 characters", "1", "mail")
    else if (username.length <= 6 || username == " ") signupNotif("Name must be atleat 7 characters", "1", "name")
    else if (!agreement) signupNotif("You must agree to terms and conditions to register", "1", "agree")
    else{
      let parts = username.split(" ")
      let fst = parts[0].toLowerCase()
      let scn = parts[1].toLowerCase()
      let un = `${fst}-${scn}-${scn.length}`
      console.log(un+un.length)
      await authService.createUser(username, email, password, agreement, un, un.length).then((res) => {
        let new2 = res['data']
        if(new2 == "Email is already in use") signupNotif(new2, "1", "mail")
        else {
          localStorage.setItem("user", JSON.stringify(new2))
          setUser(new2)
          router.push('/')
          setLoading(false)
         } 
      }).catch((error) => signupNotif(error.message, "3", "mail"))
      .finally(() => setLoading(false)) 
    }
      
  }

  const resetAuth = async (email: string) =>{
    setLoading(true)

      if (email.length <= 5) signupNotif("Email must be atleat 6 characters", "1", "mail")
      else{
        await authService.verifyAccount(email).then((res) => {
          let new2 = res['data']
         if(new2 == "Account doesn't exist") signupNotif(new2, "1", "mail")
         else {
          router.push('/verify')
          setLoading(false)
         }
        }).catch((error) => signupNotif(error.message, "3", "mail"))
        .finally(() => setLoading(false)) 
      }
  }

  const verifyCode = async (code: string, email: string, page: string) =>{
    setLoading(true)

      if (code.length <= 6) signupNotif("Verification code doesn't fit length", "1", "name")
      else{
        await authService.verifyCode(code, email).then((res) => {
          let new2 = res['data']
         if(new2 == "Code doesn't exist") signupNotif(new2, "1", "name")
         else if(new2 == "Code already expired, please resend") signupNotif(new2, "1", "name")
         else {
          router.push(page)
          setLoading(false)
         }
        }).catch((error) => signupNotif(error.message, "3", "mail"))
        .finally(() => setLoading(false)) 
      }
  }

  const resetPass = async (password: string, password2: string) =>{
    setLoading(true)

    if(password != password2) signupNotif("passwords do not match", "2", "pass")
    else if (password.length <= 8) signupNotif("passwords must be atleast 9 characters", "1", "pass")
      else{
        await authService.updatePassword(password).then((res) => {
          let new2 = res['data']
         if(new2 == "Code doesn't exist") signupNotif(new2, "1", "name")
         else {
          router.push('/')
          setLoading(false)
         }
        }).catch((error) => signupNotif(error.message, "3", "mail"))
        .finally(() => setLoading(false)) 
      }
  }

  const signWithGithub = async () => {
    //console.log('github')
    setLoading(true)
    await signInWithPopup(auth, provider)
      .then(async (userCredential) => {
        const credential = GithubAuthProvider.credentialFromResult(userCredential);
        const token = credential!.accessToken;
        setUsers(userCredential.user)
        let usr = userCredential.user
        let und = usr.displayName!.toLowerCase()
        let un = `${und}-${und.length}`
        let data = {
          "name": usr.displayName!, //str,
          "username": un, //str,
          "email": usr.email!,  //str
          "phone": usr.phoneNumber!, //str
          "picture": usr.photoURL!, //str
          "suid": usr.uid!, //str
          "tenant_id": usr.tenantId!, //str
          "verified": usr.emailVerified! //bool
        }

        await authService.socialSignup(data).then((res) => {
          router.push('/')
          setLoading(false)
        }).catch((error) => signupNotif(error.message, "3", "mail"))
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GithubAuthProvider.credentialFromError(error);
        signupNotif(error.message, "3", "mail")
      })
      .finally(() => setLoading(false))

  }

  const signWithGoogle = async () => {
    //console.log('google')
    setLoading(true)
    await signInWithPopup(auth, prov)
      .then(async(userCredential) => {
        const credential = GoogleAuthProvider.credentialFromResult(userCredential);
        const token = credential!.accessToken;
        setUsers(userCredential.user)
        let usr = userCredential.user
        let und = usr.displayName!.toLowerCase()
        let un = `${und}-${und.length}`
        let ul = und.length

        let data = {
          "name": usr.displayName!, //str,
          "username": un,
          "userlen": ul, //str,
          "email": usr.email!,  //str
          "phone": usr.phoneNumber!, //str
          "picture": usr.photoURL!, //str
          "suid": usr.uid!, //str
          "tenant_id": usr.tenantId!, //str
          "verified": usr.emailVerified!, //bool
          "created": Date.now
        }

        await authService.socialSignup(data).then((res) => {
          router.push('/')
          setLoading(false)
        }).catch((error) => signupNotif(error.message, "3", "mail"))
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
        signupNotif(error.message, "3", "mail")
      })
      .finally(() => setLoading(false))
  }

  const logout = async () => {
    setLoading(true)
    signOut(auth)
      .then(() => {
        setUser(null)
      })
      .catch((error) => signupNotif(error.message, "3", "mail"))
      .finally(() => setLoading(false))
  }

  const memoedValue = useMemo(
    () => ({ user, users, signUp, signIn, resetPass, resetAuth, signWithGithub, signWithGoogle, verifyCode, error, loading, rems, logout }),
    [user, users, error, loading, rems]
  )

  return (
    <AuthContext.Provider value={memoedValue}>
      {!initialLoading && children}
    </AuthContext.Provider>
  )
}

// Let's only export the `useAuth` hook instead of the context.
// We only want to use the hook directly and never the context comopnent.
export default function useAuth() {
  return useContext(AuthContext)
}
