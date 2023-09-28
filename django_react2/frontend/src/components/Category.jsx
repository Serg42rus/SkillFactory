import { Link } from "react-router-dom";
import { useState, useEffect } from "react";


const Category = () => {
    
    const [listOfCategory, setListOfCategory] = useState([]);
    
    useEffect(()=> {
            fetch(`http://127.0.0.1:8000/category/`)
            .then(response => response.json())
            .then(data => setListOfCategory(data))          
    }, []);
        
            return (
                <div>
                    <h3> категории </h3>
                
                    { 
                        listOfCategory.map(Reciept=> (                        
                            <Link key={Reciept.title} to={`/Cook_Book/${Reciept.id}` }>
                                <li>{Reciept.title}</li>
                                    Читать рецепт полностью
                            </Link>
                        )) 
                    }
                </div>
        );
          
        }     
    

export {Category};
