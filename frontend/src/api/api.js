import axios from 'axios'

axios.defaults.baseURL = process.env.ROOT_API
let HTTP = axios.create({
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
})

export const Posts = {
  getPosts () {
    return HTTP.get('https://jsonplaceholder.typicode.com/posts').then(responce => {
      return responce.data
    }).catch(error => {
      console.log(error)
    })
  },
  getPost (id) {
    return HTTP.get('https://jsonplaceholder.typicode.com/posts/' + id).then(responce => {
      return responce.data
    }).catch(error => {
      console.log(error)
    })
  }
}
