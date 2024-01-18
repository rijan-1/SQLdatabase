import { UserContext } from "./UserContext"
import {useState, useContext} from 'react'

export const Register = () => {
    const {setToken} = useContext(UserContext)

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [confirmationPassword, setConfirmationPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')

  return <div>
  <h1>Registration page</h1>

  <div>
    <input type='email' placeholder='enter email' value={email} onChange={(e)=>setEmail(e.target.value)} required/>
    <input type='password' placeholder='enter password' value={password} onChange={(e)=>setPassword(e.target.value)} required/>
    <input type='password' placeholder='enter password' value={confirmationPassword} onChange={(e)=>setConfirmationPassword(e.target.value)} required/>

  </div>
  <br/>
  <button type='submit'>Submit</button>
      
    </div>
  
}


