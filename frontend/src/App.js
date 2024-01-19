import './App.css'
import {useEffect, useState} from 'react'
import { Register } from './components/Register';
const App = () => {

  const [message, setMessage] = useState('')
  useEffect(()=>{

  const getWelcomeMessage = async()=>{

    const requestOptions ={
      method: 'GET',
      headers:{
        'content-type':'application/json'
      }
    }
    const response = await fetch('http://localhost:8000/api', requestOptions)
    const data = await response.json()

    if (!response.ok){
      console.log('error while getting api')
    }
    else{
    setMessage(data.idk)
 } }
  getWelcomeMessage()
},[])
  return (
    <div>

    
    <h1>Hello world</h1>
    <h1>{message}</h1>
    <Register/>
   </div>
  )
};

export default App;