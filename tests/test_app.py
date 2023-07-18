from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
Once a user is logged in, they see the homepage where they can choose to list or book a space
"""
def test_load_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/homepage")
    heading = page.locator('h1')
    expect(heading).to_have_text('What would you like to do?')
    link_to_book = page.locator('.t-book')
    expect(link_to_book).to_have_text("Book a space")