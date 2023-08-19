import React, { useState, useEffect } from 'react';
import { Link, useParams } from "react-router-dom";

function Reciept () {
    let params = useParams();
    let category = params.category;
    let backway = "/" + category
    let index = params.index;

    const [listOfCatigory, setListOfCatigory] = useState();
    useEffect(()=> {
        fetch(`http://127.0.0.1:8000/api/cook_book`)
        .then(response => response.json())
        .then((result) => {
        setListOfCatigory(result)})          
    }, [category]);
      
    if (listOfCatigory) {
        const name = listOfCatigory[index].name;
        const category = listOfCatigory[index].category;
        const text = listOfCatigory[index].text;
        return <div>
             <h3>{ name }</h3>
             <h2>{ category }</h2>
             <p>{ text }</p>
             <Link to= { backway } > Вернуться к списку рецептов </Link>
        </div>
    } else {
        return <div>
             <Link to= { backway } >  Вернуться к списку рецептов </Link>
        </div>
    }
}

export default Reciept;