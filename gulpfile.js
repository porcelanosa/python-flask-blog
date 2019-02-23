'use strict';
var gulp = require('gulp'),
    watch = require('gulp-watch'),
    prefixer = require('gulp-autoprefixer'),
    uglify = require('gulp-uglify'),
    babel = require('gulp-babel'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    concat = require('gulp-concat'),
    rename = require('gulp-rename'),
    cleanCSS = require('gulp-clean-css'),
    plumber = require('gulp-plumber'),
    pump = require('pump'),
    notify = require('gulp-notify');

var path = {
  build: {
    js: 'blog/static/js/',
    css: 'blog/static/css/',
  },
  src: {
    js: 'blog/static/js/app.js',
    style: 'blog/static/css/scss/style.scss',
  },
  watch: {
    js: 'blog/static/js/app.js',
    style: 'blog/static/css/scss/**/*.scss',
  },
};
// Set the browser that you want to support
const AUTOPREFIXER_BROWSERS = [
  'ie >= 10',
  'ie_mob >= 10',
  'ff >= 30',
  'chrome >= 34',
  'safari >= 7',
  'opera >= 23',
  'ios >= 7',
  'android >= 4.4',
  'bb >= 10',
];
gulp.task('js:build', function(cb) {
  pump([
        gulp.src(path.src.js),
        sourcemaps.init(),
        babel({
          presets: ['@babel/env']
        }),
        uglify(),
        //concat('all.js')).
        rename({
          suffix: '.min',
        }),
        sourcemaps.write('.'),
        gulp.dest(path.build.js),
      ],
      cb,
  );
});

gulp.task('style:build', function() {
  gulp.src(path.src.style).
      pipe(plumber({
        errorHandler: function(err) {
          notify.onError({
            title: 'Gulp error in ' + err.plugin,
            message: err.toString(),
          })(err);
        },
      })).
      pipe(sourcemaps.init()).
      pipe(sass({
        outputStyle: 'compressed',
        sourceMap: false,
        errLogToConsole: true,
      })).
      pipe(prefixer({browsers: AUTOPREFIXER_BROWSERS})).
      pipe(cleanCSS({level: 2})).
      pipe(sourcemaps.write('.')).
      pipe(gulp.dest(path.build.css));
});
/*

gulp.task('image:build', function() {
  gulp.src(path.src.img).pipe(cache(imagemin({
    progressive: true,
    svgoPlugins: [{removeViewBox: true}],
    //use: [pngquant()],
    interlaced: true,
  }))).pipe(gulp.dest(path.build.img)).pipe(reload({stream: true}));
});
gulp.task('svgsprites', function() {
  return gulp.src(path.src.svgicons).pipe(svgmin()).pipe(svgSymbols(
      {
        slug: function(name) {
          return 'svgicon-' + name.replace(/\s/g, '-');
        },
        svgClassname: 'svg-icon-lib',
      },
  )).pipe(gulp.dest(path.build.svgicons));
});
gulp.task('fonts:build', function() {
  gulp.src(path.src.fonts).pipe(gulp.dest(path.build.fonts));
});
*/

gulp.task('build', [
  //'html:build',
  'js:build',
  'style:build',
  /*'fonts:build',
  'image:build'*/
]);

gulp.task('watch', function() {
  /*watch([path.watch.html], function(event, cb) {
    gulp.start('html:build');
  });*/
  watch([path.watch.style], function(event, cb) {
    gulp.start('style:build');
  });
  watch([path.watch.js], function(event, cb) {
    gulp.start('js:build');
  });
  /*watch([path.watch.img], function(event, cb) {
    gulp.start('image:build');
  });
  watch([path.watch.fonts], function(event, cb) {
    gulp.start('fonts:build');
  });*/
});

//gulp.task('default', ['build', 'webserver', 'watch']);
gulp.task('default', ['watch']);
