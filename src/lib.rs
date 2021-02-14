extern crate pyo3;
use pyo3::exceptions;
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

extern crate cumin;
use cumin::eval::eval;
use cumin::parser::cumin::cumin;

macro_rules! raise {
    ($( $params:expr ),*) => {
        Err(exceptions::PySystemError::new_err(format!( $( $params ),*)))
    };
}

#[pyfunction]
fn load(source: &str) -> PyResult<String> {
    match cumin(source) {
        Ok((rest, data)) => {
            if rest == "" {
                match eval(data, None) {
                    Ok(data) => Ok(data.stringify()),
                    Err(err) => raise!("Error: eval failed ({:?})", err),
                }
            } else {
                raise!("Error: Parsing stopped at {}", &rest)
            }
        }
        Err(err) => raise!("Error: Parsing failed ({:?})", &err),
    }
}

#[pymodule]
fn cumin_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(load, m)?)?;
    Ok(())
}
