use leptos::*;
use reqwest::get;
use leptos::logging::log;

async fn get_visit_count() -> String {
    let r: String = reqwest::get("http://127.0.0.1:5000/add_1")
        .await
        .expect("could not get requests")
        .text()
        .await
        .expect("could not get text");
    r.trim().to_string()
}

#[component]
fn App() -> impl IntoView {
    // let (visits_json, set_visits_json) = create_signal("".to_string());

    let resp = create_resource(|| (), |_| async move { get_visit_count().await });
    // move || set_visits_json.set(resp.get().unwrap_or_default());
    view! {
        <div class:container=true>
            <span>you are person</span>
            <br/>
            <span class:visit_count=true>{move || format!("{}", resp.get().unwrap_or_default() )}</span>

            <br/>
            <span>to visit on this site</span>
        </div>
    }
}

fn main() {
    leptos::mount_to_body(move || view! { <App/> })
}
