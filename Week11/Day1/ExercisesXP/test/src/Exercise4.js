import React from 'react';
import './Exercise4.css';

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };

class Exercise4 extends React.Component {
    render() {
        return (
            <div>
                <h1 style={style_header}>This is a Header</h1>
                <p className='para'>This is a Paragraph</p>
                <a href='/'>This is a Link</a>
                <form>
                    <strong>This is a Form</strong><br />
                    <label for="name">Enter your name:</label>
                    <input type="text" id="name" name="name" />
                    <input type="submit" value="Submit" />
                </form>
                <img src='https://diatomenterprises.com/wp-content/uploads/2022/09/reactJS_logo.jpeg' alt='React Logo' />
                <ul>
                    <strong>This is a list:</strong>
                    <li>Coffee</li>
                    <li>Tea</li>
                    <li>Milk</li>
                </ul>
            </div>
        
        );
    }
}

export default Exercise4;