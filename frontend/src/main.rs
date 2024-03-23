use leptos::*;
use reqwest::get;
use leptos::logging::log;

#[component]
fn App() -> impl IntoView {
    let resp = create_resource(|| (), |_| async move { 
        let r: String = reqwest::get("http://127.0.0.1:5000/add_1")
            .await
            .expect("could not get requests")
            .text()
            .await
            .expect("could not get text");
        r
    });
    
    view! {
        <p> sdf {format!("{:?}", resp.get())}</p>
    }
}

fn main() {
    leptos::mount_to_body(move || view! { <App/> })
}
