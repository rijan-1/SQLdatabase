import { createContext, useState } from "react";

import React from 'react'

export  const UserContext = createContext()

export const UserProvider =(props) => {
    const [token, setToken] = useState(localStorage.getItem('Aweseom user leads'))
    useEffect(()=>{

      
        const fetchUser = async()=>{
              const requestOptions={
            method:'GET',
            headers:{
                'content-type':'application/json',
                Authorization:'Bearer'+ token
            }
        }
        const reponse = ('https://localhost:8000/api/users/me', requestOptions)
      
        if (!reponse.ok){
            setToken(null)
        }
        localStorage.setItem('Aweseom user leads', token)

        }
        fetchUser()

    },[token])
  return (
   <UserContext.Provider value={{token, setToken}}>
    {Children.props}
   </UserContext.Provider>
  
      
    
  )
}


