import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { store } from './reducers';

const render = function() {
  ReactDOM.render(<App />, document.getElementById("root"))
} 

render()

store.subscribe(render);
