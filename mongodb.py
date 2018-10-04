def config(app):
    app.config.update(
        MONGO_URI="mongodb://admin:r00t_mdbtj@ds039261.mlab.com:39261/project-books-tj",
        MONGODB_NAME="project-books-tj"
    )