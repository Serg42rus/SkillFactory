import React from 'react';
import {Routes, Route } from 'react-router-dom';
import {Reciept} from './components/Reciept';
import Layout from './components/Layout'
import {Category} from './components/Category';
import SingleReciept from './components/SingleReciept';


function App() {
  return (
    <div className='app'>    
      <main>
      <Routes>
        <Route path="/"element={<Layout/>}>
          <Route index element={<Reciept/>}></Route>
          <Route path="category/" element={<Category/>}></Route>
          <Route path="Cook_Book/:id" element={<SingleReciept/>}></Route>
        </Route>  
      </Routes>
      </main>
    </div>
  );
}

export {App};