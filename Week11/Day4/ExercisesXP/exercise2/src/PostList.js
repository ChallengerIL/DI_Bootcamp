import { Component } from 'react';
import jsonData from './posts.json';

class PostList extends Component {
    render() {
        return(
            <ul>
                {jsonData.map(post => {
                    return (
                        <li key={post.id}>
                            <h2>{post.title}</h2>
                            <p>{post.content}</p>
                        </li>
                    );
                })}
            </ul>
        );
    };
};

export default PostList;
