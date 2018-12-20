const gulp = require('gulp');
const yml = require('gulp-yaml');

gulp.task('build', () => {
    return gulp.src('./cdn.yml')
        .pipe(yml({
            schema: 'DEFAULT_SAFE_SCHEMA',
            space: 2,
        }))
        .pipe(gulp.dest('./dist/'))
});

gulp.task('default', gulp.parallel('build'));
