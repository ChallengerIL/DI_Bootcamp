import { Component } from 'react';
import jsonData from './data.json';

class Example1 extends Component {
    render() {
        return(
            jsonData.SocialMedias.map((link, index) => {
                return(
                <li key={index}>{link}</li>
                )
            })
        );
    };
};

export default Example1;
