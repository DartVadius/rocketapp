new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        posts: [],
        loading: false,
        currentPost: {},
        message: null,
        newPost: {'post_heading': null, 'post_body': null},
    },
    mounted: function () {
        this.getPosts();
    },
    methods: {
        getPosts: function () {
            this.loading = true;
            this.$http.get('/api/v1/posts/')
                .then((response) => {
                    console.log(response);
                    this.posts = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPost: function (id) {
            this.loading = true;
            this.$http.get('/api/v1/posts/${id}/')
                .then((response) => {
                    this.currentPost = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
    }
});