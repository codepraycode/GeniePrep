import React from 'react';
import { Link } from 'react-router-dom';

const Records = () => {
    return (
        <div className="records section card container">
            <h4 className="lead">Previous Records</h4>

            <table className="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">S\N</th>
                        <th scope="col">Course</th>
                        <th scope="col">% Score</th>
                        <th scope="col">Date</th>
                        <th scope="col"></th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <th scope="row">1</th>
                        <td>Course 1</td>
                        <td>80%</td>
                        <td>12/05/2022</td>
                        <td>
                            <Link to={`/result/${12}`}>
                                {/* <i className="fa-solid fa-file-chart-column"></i> */}
                                <i className="fa fa-eye" aria-hidden="true"></i>
                            </Link>
                        </td>
                    </tr>

                    <tr>
                        <th scope="row">2</th>
                        <td>Course 1</td>
                        <td>80%</td>
                        <td>12/05/2022</td>
                        <td>
                            <Link to={`/result/${12}`}>
                                {/* <i className="fa-solid fa-file-chart-column"></i> */}
                                <i className="fa fa-eye" aria-hidden="true"></i>
                            </Link>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    );
};

export default Records;