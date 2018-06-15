import { HTTP} from "./common";

export const Posts = {
  list() {
    return HTTP.get('/posts/').then(response => {
      return response.data
    })
  },
  get() {
    return HTTP.get('/posts/${post.id}/').then(response => {
      return response.data
    })
  }
};
