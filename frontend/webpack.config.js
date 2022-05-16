const path = require('path');
const webpack = require('webpack');


module.exports = (env, argv) => {
    const mode = argv.mode || 'development';

    return {
        mode,
        entry: "./src/index.js",
        output: {
            path: path.resolve(__dirname, "../static/js"),
            filename: "[name].js",
        },
        module: {
            rules: [{
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                },
            }, ],
        },
        optimization: {
            minimize: true,
        },
        plugins: [
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify(mode)
            })
            // new webpack.DefinePlugin({
            //     "process.env": {
            //         // This has effect on react lib size
            //         NODE_ENV: JSON.stringify('production'),
            //     },
            // }),
        ],
    };
}

//"start": "webpack --mode development --watch",