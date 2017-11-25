extern crate rand;

use std::io;
use rand::distributions::{IndependentSample, Range};

fn main() {
    println!("Number of Samples: ");
    let mut input_text = String::new();
    io::stdin()
        .read_line(&mut input_text);

    let num_samples: u64 = input_text.trim().parse::<u64>().expect("invalid input");

    let mut num_within_radius = 0;

    let between = Range::new(0., 1.);
    let mut rng = rand::thread_rng();

    for _ in 0..num_samples {
        let x: f64 = between.ind_sample(&mut rng);
        let y: f64 = between.ind_sample(&mut rng);
        if (x*x + y*y).sqrt() <= 1. {
            num_within_radius += 1;
        }
    }

    println!("{}", 4. * (num_within_radius as f64) / (num_samples as f64));
}
