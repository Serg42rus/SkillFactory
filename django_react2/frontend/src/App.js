import './App.css';
import axios from 'axios';
import React from 'react';

class App extends React.Component{
  state = { details:[], }

  componentDidMount (){
    let data;
    axios.get('http://localhost:8000/api/cook_book')
    .then(res =>{
      data = res.data;
      this.setState({
        details: data
      });
    })
    .catch(err =>{
      console.log(err);
    })
  }
  render() {
    return (
      <div>
        <header>данные из Django</header>
        <hr></hr>
        {this.state.details.map((Cook_recepte, id) =>(
          <div key={id}>
            <div>
              <h2>{Cook_recepte.name}</h2>
              <p>{Cook_recepte.category}</p>
              <p>{Cook_recepte.text}</p>
            </div>
          </div>
        ))}
      </div>
    )
  }
}

export default App;
