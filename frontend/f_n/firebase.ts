// Import the functions you need from the SDKs you need
import { initializeApp, getApp, getApps } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCDuGaIhulAulTrBbSmCX_Gj3p5xAMvhhQ",
  authDomain: "personal-soucing.firebaseapp.com",
  projectId: "personal-soucing",
  storageBucket: "personal-soucing.appspot.com",
  messagingSenderId: "988531739927",
  appId: "1:988531739927:web:127301d1795e27ab707b52",
  measurementId: "G-K28THQPYME"
};
// Initialize Firebase
const app = !getApps().length ? initializeApp(firebaseConfig) : getApp()
const db = getFirestore()
const auth = getAuth()

export default app
export { auth, db }  
