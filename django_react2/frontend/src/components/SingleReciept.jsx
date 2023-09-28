import { useParams, Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";


const SingleReciept = () => {
    const {id} = useParams();
    const Navigate =useNavigate();
    const [Recept, setRecept] = useState(null);
    const back = () => Navigate(-1);

    useEffect(()=> {
        fetch(`http://127.0.0.1:8000/Cook_Book/${id}`)
        .then(response => response.json())
        .then(data => setRecept(data))          
}, [id]);
    
    return(
        <div>
           {Recept &&(
            <>
            <h1>{Recept.name}</h1>
            <h3>{Recept.category}</h3>
            <p>{Recept.text}</p>
            </>
           )}
           <Link onClick={ back }> Вернуться к списку рецептов </Link>
        </div>
    )
}

export default SingleReciept;
