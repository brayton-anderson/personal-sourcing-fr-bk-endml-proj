
class userService {

    getUserData = async (key: string) =>{
        let str = await localStorage.getItem(key)
        let jstr = JSON.parse(str!)
        //console.log(jstr['user']['email'])
        return jstr
    }
}
export default new userService()


