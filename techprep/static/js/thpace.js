// thpace setup for homepage hero animation
const canvas = document.querySelector('#hero-image');

const settings = {
  // Settings
  colors: ['#00a7f5', '#304d30', '#00f504'],
  triangleSize: 100,
  pointAnimationSpeed: 10000,
  particleSettings: {
    interval: 5000,
    color: "#CCCCCC"
  }

};

Thpace.create(canvas, settings);