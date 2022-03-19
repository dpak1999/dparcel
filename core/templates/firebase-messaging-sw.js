/** @format */

importScripts('https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js');

firebase.initializeApp({
  apiKey: 'AIzaSyDj6YRuM6i-h6EgWr3M6H-f4EImXaZrO4k',
  authDomain: 'dparcel-aeb5e.firebaseapp.com',
  projectId: 'dparcel-aeb5e',
  storageBucket: 'dparcel-aeb5e.appspot.com',
  messagingSenderId: '566105382238',
  appId: '1:566105382238:web:3a0915294c54d2cb5a43cf',
});

const messaging = firebase.messaging();
