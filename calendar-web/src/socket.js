import io from 'socket.io-client'

const socket = process.env.NODE_ENV === 'development' ? io('ws://127.0.0.1:2608') : io('ws://106.14.26.226:2608');
// const socket = io('ws://127.0.0.1:23810');
export default socket
