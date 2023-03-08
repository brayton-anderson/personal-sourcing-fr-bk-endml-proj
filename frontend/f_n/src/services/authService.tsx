import axios, { formToJSON } from 'axios';
import { json } from 'react-router-dom';

const API_BASE_URL = "http://localhost:5000/";
let headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin" : "*",
    "accept": "application/json",
    "Connection": "keep-alive",
    "Accept-Encoding":"gzip, deflate, br",
    "Access-Control-Allow-Methods":"GET,PUT,POST,DELETE,PATCH,OPTIONS"   
};


// /login
class authService {

    signIn = async (usr: string, pass: string) => {
        const data = {
            "username": usr,
            "password": pass
        }
        // console.log(email)

        //console.log(JSON.parse(JSON.stringify(data)))
         const newww = await fetch(API_BASE_URL+'login', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
        // axios.get(API_BASE_URL);
    }

    createUser = async (usr: string, eml: string,  pass: string, agreement: boolean, un: string, len: any) =>{
        const data = {
            "username": usr,
            "email": eml,
            "password": pass,
            "agreement": agreement,
            "name": un,
            "userlen": len,
            "verified": false,
            "created-at": Date.now()
        }

        //console.log(JSON.parse(JSON.stringify(data)))
         const newww = await fetch(API_BASE_URL+'sign-up', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
    }

    socialSignup = async(data: any) =>{
        const newww = await fetch(API_BASE_URL+'social-signup', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
    }

    verifyAccount = async(email: string) =>{
        let data = {
            "email": email,
            "created_at": Date.now
        }
        const newww = await fetch(API_BASE_URL+'verify-email', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
    }

    verifyCode = async(code: string, email: string) =>{
        let data = {
            "code": code,
            "email": email
        }
        const newww = await fetch(API_BASE_URL+'verify-code', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
    }

    updatePassword = async(password: string) =>{
        let data = {
            "password": password
        }
        const newww = await fetch(API_BASE_URL+'social-signup', {
            method: 'POST',
            headers: headers,
            body:JSON.stringify(data),  
          }).then((response) => response.json())
        // console.log(newww)
        return newww
    }

    updateUser(user: any, userId: string){
        return axios.put(API_BASE_URL + '/' + userId, user);
    }

    deleteUser(userId: string){
        return axios.delete(API_BASE_URL + '/' + userId);
    }
}

export default new authService()