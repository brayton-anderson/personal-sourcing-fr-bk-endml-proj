import toast, { Toaster } from 'react-hot-toast'

const toastStyle = {
    background: 'white',
    color: 'black',
    fontWeight: 'bold',
    fontSize: '16px',
    padding: '15px',
    borderRadius: '9999px',
    maxWidth: '1000px',
  }

  //

const signupNotification = (notif: string, designator: string, prov: string) =>{
if (designator == "1"){
   document.getElementById(prov)!.style.setProperty("border-color", "rgb(249 115 22/1)")
   document.getElementById(prov)!.style.setProperty("border-width", "2px")
   toast(notif,{duration: 2000, style: toastStyle,}
  )
}else if(designator == "2"){
    document.getElementById(prov+'r')!.style.setProperty("border-color", "rgb(249 115 22/1)")
    document.getElementById(prov)!.style.setProperty("border-color", "rgb(249 115 22/1)")
    document.getElementById(prov+'r')!.style.setProperty("border-width", "2px")
    document.getElementById(prov)!.style.setProperty("border-width", "2px")
    toast(notif,{duration: 2000, style: toastStyle,})  
}else{
  toast(notif,{duration: 2000, style: toastStyle,})
}

}

export default signupNotification