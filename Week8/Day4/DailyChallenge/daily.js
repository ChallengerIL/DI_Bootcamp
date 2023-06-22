// Instructions
// In this exercise, you will use object oriented programming concepts to define and use a custom object in JavaScript.

// Create a class named Video. The class should be constructed with the following parameters:
// title (a string)
// uploader (a string, the person who uploaded it)
// time (a number, the duration of the video - in seconds)
// Create a method called watch() which displays a string as follows:
// “uploader parameter watched all time parameter of title parameter!”
// Instantiate a new Video instance and call the watch() method.
// Instantiate a second Video instance with different values.
// Bonus: Use an array to store data for five Video instances (ie. title, uploader, time)
// Think of the best data structure to save this information within the array.
// Bonus: Loop through the array to instantiate those instances.

class Video {
    constructor(title, uploader, time) {
      this.title = title;
      this.uploader = uploader;
      this.time = time;
    }

    watch() {
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`);
    }
}

let video1 = new Video('Some title', 'Some uploader', 10);
video1.watch();

let video2 = new Video('Another title', 'Another uploader', 20);
video2.watch();

const paramsArray = [['title1', 'uploader1', 10], ['title2', 'uploader2', 20], ['title3', 'uploader3', 30], ['title4', 'uploader4', 40], ['title5', 'uploader5', 50]];

for (let params of paramsArray) {
    let video = new Video(params[0], params[1], params[2]);
    video.watch();
}
