import { Component } from 'react';
import jsonData from './data.json';

class Example2 extends Component {
    render() {
        return(
            jsonData.Skills.map(item => {
                return (
                <ul>
                    <strong>{item.Area}</strong>
                    {item.SkillSet.map((item, index) => {
                        return <li key={index}>{item.Name}</li>
                    })}
                </ul>
                )
            })
        );
    };
};

export default Example2;
