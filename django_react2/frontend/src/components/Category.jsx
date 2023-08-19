import React, { useState, useEffect } from 'react';
import { useParams, Link, useLocation } from "react-router-dom";

function Category () {
    let params = useParams();
    let category = params.category;
    
    const catDict = {
        soup: "первое блюдо",
        main: "Основное блюдо",
        desert: "Десерт",
    }
    
    const location = useLocation();
    const [listOfCategory, setListOfCategory] = useState();

    useEffect(()=> {
            fetch(`http://127.0.0.1:8000/api/cook_book`)
            .then(response => response.json())
            .then((result) => {
            setListOfCategory(result)})          
    }, [category]);

    if (listOfCategory) {
        return (
            <div>
                <h3> { catDict[category] } </h3>
                { listOfCategory.map((Reciept, index)=> {
                    return <>
                        <div key={ index }>
                        {Reciept.category} |
                        <Link to= {location.pathname + "/" + index }> рецепт </Link>
                        </div>
                        </>
                }) }
            </div>
        );
    } else {
        return (
            <div>
                { category }
            </div>
        );
    }

}

export default Category;