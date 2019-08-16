import React, { Component } from 'react';
import {Route} from 'react-router-dom';
import LoginPage from './views/LoginPage';
import Styles from './styles/main.scss';
import MainPage from './views/Main/Main';
import Restaurants from './views/Restaurants/Restaurants';

class App extends Component {
  render() {
    return (
      <div style={{height: '100vh'}}>
        <Route path="/login" exact component={LoginPage}/>
        <Route path="/" exact component={MainPage}/> 
        <Route path="/restaurants" exact component={Restaurants}/> 

      </div>
    );
  }
}

export default App;
