import React from 'react';

import { Link, Routes, Route } from 'react-router-dom';
import Category from './components/Category';
import Reciept from './components/Reciept';


function App() {
  return (
    <div>
      <header>
        <h1>Книга рецептов</h1>
        <Link to="/">Главная</Link>
        <Link to="soup">первое блюдо</Link>
        <Link to="main">основное блюдо</Link>
        <Link to="desert">десерт</Link>
      </header>
      
      <main>
      <Routes>
          <Route path="/"></Route>
          <Route path=":category" element={<Category/>}></Route>
          <Route path=":category/:index" element={<Reciept/>}></Route>
      </Routes>
      </main>
    </div>
  );
}

export default App;