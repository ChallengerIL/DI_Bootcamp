import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// // 1.1
// const nojsx = React.createElement('h1', {}, 'I do not use JSX');
// root.render(nojsx, document.getElementById('root'));

// // 2.1
// root.render(<p>Hello world!</p>, document.getElementById('root'));

// // 2.2
// const withjsx = <h1>I Love JSX!</h1>;
// root.render(withjsx, document.getElementById('root'));

// // 2.3
// const sum = 5 + 5
// root.render(<h1>React is {sum} times better with JSX</h1>, document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
