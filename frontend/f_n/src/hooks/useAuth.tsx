import axios from 'axios';
import authService from '../services/authService'
import toast, { Toaster } from 'react-hot-toast'
import  signupNotif from '../utils/utils'

import {
    createUserWithEmailAndPassword,
    onAuthStateChanged,
    signInWithEmailAndPassword,
    signOut,
    User,
  } from 'firebase/auth'

  const toastStyle = {
    background: 'white',
    color: 'black',
    fontWeight: 'bold',
    fontSize: '16px',
    padding: '15px',
    borderRadius: '9999px',
    maxWidth: '1000px',
  }

class useAuth {
    

    signIn = async (username: string, _password: string, rem: boolean) => {
      if (_password.length <= 8) signupNotif("passwords must be atleast 9 characters", "1", "pass")
      else if (username.length <= 5) signupNotif("Email must be atleat 6 characters", "1", "mail")
      else{
        let newww = await authService.signIn(username, _password)
         let new2 = newww['data']
         if(new2 == "wrong username") signupNotif(new2, "1", "mail")
         else if(new2 == "wrong password" ) signupNotif(new2, "1", "pass")
         else localStorage.setItem("user", JSON.stringify(new2))
         console.log(new2)
        return new2  
      }
    }

    signUp= async (username: string, email: string,  _password: string, _password2:string, agreement: boolean) =>{
       
        if(_password != _password2) signupNotif("passwords do not match", "2", "pass")
        else if (_password.length <= 8) signupNotif("passwords must be atleast 9 characters", "1", "pass")
        else if (email.length <= 5) signupNotif("Email must be atleat 6 characters", "1", "mail")
        else if (username.length <= 6 || username == " ") signupNotif("Name must be atleat 7 characters", "1", "name")
        else if (!agreement) signupNotif("You must agree to terms and conditions to register", "1", "agree")
        else{
            let parts = username.split(" ")
            let fst = parts[0].toLowerCase()
            let scn = parts[1].toLowerCase()
            let un = `${fst}-${scn}-${scn.length}`
            console.log(un+un.length)
            let newww = await authService.createUser(username, email, _password, agreement, un, un.length)
            let new2 = newww['data']
          // console.log(new2)
            
            if(new2 == "Email is already in use") signupNotif(new2, "1", "mail")
            else localStorage.setItem("user", JSON.stringify(new2))
          
          return new2
        }
    }

    getUserById(userId: string){
        return axios.get( + '/' + userId);
    }

    updateUser(user: any, userId: string){
        return axios.put( + '/' + userId, user);
    }

    deleteUser(userId: string){
        return axios.delete( + '/' + userId);
    }
}

export default new useAuth()