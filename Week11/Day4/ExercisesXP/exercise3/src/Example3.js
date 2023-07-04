import { Component } from 'react';
import jsonData from './data.json';

class Example3 extends Component {
    render() {
        return(
            jsonData.Experiences.map((item, index) => {
                return (
                <div key={index}>
                    <img src={item.logo} alt={item.companyName} width="150px"></img><br />
                    <a href={item.url}>{item.companyName}</a>
                    {item.roles.map(role => {
                        return (
                            <div>
                                <p><strong>{role.title}</strong></p>
                                <p>{role.startDate} {role.location}</p>
                                <p>{role.description}</p>
                            </div>
                        )
                    })}
                </div>
                )
            })
        );
    };
};

export default Example3;
