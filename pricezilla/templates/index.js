// var classList = document.getElementById('navscroll').classList;

// var maxWidth576 = window.matchMedia("(max-width: 576px)");
// var windowSize = window.innerWidth;

// function tolu()
// { (windowSize >=576) ? classList.remove('container') : classList.add('container')}

const puppeteer = require("puppeteer");

(async () => {
    const browser = await puppeteer.launch({headless:false});
    const page = await browser.newPage()
    await page.goto("https://www.jumia.com.ng/");
    await page.screenshot({ path: "prices.png" });

    const 

    await browser.close();
})();