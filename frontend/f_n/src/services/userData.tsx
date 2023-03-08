import Users from '../services/userService'
export declare interface UserData {
    id: number
    email: string
    username: string
    name: string
    phone_number: number
    agreement: boolean
    verified: boolean
}
const auth =  Users.getUserData("user")
export { auth }