import './App.css';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';

// class DemoCarousel extends Component {
//     render() {
//         return (
//             <Carousel>
//                 <div>
//                     <img src="assets/1.jpeg" />
//                     <p className="legend">Legend 1</p>
//                 </div>
//                 <div>
//                     <img src="assets/2.jpeg" />
//                     <p className="legend">Legend 2</p>
//                 </div>
//                 <div>
//                     <img src="assets/3.jpeg" />
//                     <p className="legend">Legend 3</p>
//                 </div>
//             </Carousel>
//         );
//     }
// });

// ReactDOM.render(<DemoCarousel />, document.querySelector('.demo-carousel'));

function App() {
  return (
    <Carousel>
        <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg" alt='Hong Kong' />
            <p className="legend">Hong Kong</p>
        </div>
        <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp" alt='Macao' />
            <p className="legend">Macao</p>
        </div>
        <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp" alt='Japan' />
            <p className="legend">Japan</p>
        </div>
        <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp" alt='New York' />
            <p className="legend">New York</p>
        </div>
    </Carousel>
  );
}

export default App;
