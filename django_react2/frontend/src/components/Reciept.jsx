import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";


const Reciept = () => {
  
    const [listOfCategory, setListOfCategory] = useState([]);

    useEffect(()=> {
            fetch(`http://127.0.0.1:8000/Cook_Book/`)
            .then(response => response.json())
            .then(data => setListOfCategory(data))          
    }, []);
        
            return (
                <div>
                    <h3> категории </h3>
                
                    { 
                        listOfCategory.map(Reciept=> (                        
                            <Link key={Reciept.category} to={`/Cook_Book/${Reciept.id}` }>
                                <li>{Reciept.name}</li>
                                    Читать рецепт полностью
                            </Link>
                        )) 
                    }
                </div>
        );
          
        }     
    

export {Reciept};