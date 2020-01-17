const gulp = require('gulp');
const yml = require('gulp-yaml');
const htmlmin = require("gulp-htmlmin");
const htmlclean = require("gulp-htmlclean");

const yml2json = () => {
    return gulp.src('./src/cdn.yml')
        .pipe(yml({
            schema: 'DEFAULT_SAFE_SCHEMA',
            space: 2,
        }))
        .pipe(gulp.dest('./dist/'));
}

const minifyHTML = () => {
    return gulp.src('src/*.html')
        .pipe(htmlmin({
            removeComments: true,
            minifyJS: true,
            minifyCSS: true,
            collapseWhitespace: true
        }))
        .pipe(htmlclean())
        .pipe(gulp.dest('dist'));
}

exports.minifyHTML = minifyHTML;
exports.yml2json = yml2json;

gulp.task('build', gulp.series(
    yml2json,
    minifyHTML
));

gulp.task('default', gulp.parallel('build'));
