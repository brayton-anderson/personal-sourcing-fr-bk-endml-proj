import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000";
let headers: {
    "Content-Type": 'application/json',
    'Access-Control-Allow-Origin' : '*',
    "Accept": '*/*',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate, br'
    'Access-Control-Allow-Methods':'GET,PUT,POST,DELETE,PATCH,OPTIONS',   
};
// /login
class authService {

    signIn = async (usr: string, pass: string) => {
        // console.log(email)
        
        let data = {
            'username': usr,
            'password': pass,
        }

        console.log(JSON.parse(JSON.stringify(data)))
         const newww = await fetch(API_BASE_URL+'/login', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data),
          }).then((response) => response.json())
         console.log(newww)
        return newww
        // axios.get(API_BASE_URL);
    }

    getUsers(){
        return axios.get(API_BASE_URL);
    }

    createUser(user: any){
        return axios.post(API_BASE_URL, user);
    }

    getUserById(userId: string){
        return axios.get(API_BASE_URL + '/' + userId);
    }

    updateUser(user: any, userId: string){
        return axios.put(API_BASE_URL + '/' + userId, user);
    }

    deleteUser(userId: string){
        return axios.delete(API_BASE_URL + '/' + userId);
    }
}

export default new authService()