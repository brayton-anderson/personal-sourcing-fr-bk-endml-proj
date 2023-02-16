import axios from 'axios';
import authService from '../services/authService'


class useAuth {

    signIn = async (username: string, _password: string) => {
         let newww = await authService.signIn(username, _password)
        return newww
    }

    signUp(username: string, _password: string){
        console.log(username)
        return 
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