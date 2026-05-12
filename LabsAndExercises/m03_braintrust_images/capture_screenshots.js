/**
 * Braintrust Screenshot Capture Script
 *
 * Run this once from Terminal to capture all screenshots for the M03 activity guide.
 * It opens a browser window, waits for you to log in, then auto-captures all pages.
 *
 * Prerequisites:
 *   npm install playwright
 *   npx playwright install chromium
 *
 * Usage:
 *   node capture_screenshots.js
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUTPUT_DIR = path.dirname(__filename); // saves to same folder as this script
const ORG = 'AgenticCourse';
const PROJECT = 'My%20Project';
const BASE = `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}`;

const PAGES = [
  {
    name: '01_project_overview',
    url: BASE,
    wait: 'networkidle',
    desc: 'Project overview + left nav',
    clip: null  // full page
  },
  {
    name: '02_datasets_create',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/datasets`,
    wait: 'networkidle',
    desc: 'Datasets page — Create button',
    clip: null
  },
  {
    name: '03_dataset_row_editor',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/datasets`,
    wait: 'networkidle',
    desc: 'Dataset row editor (input + expected columns)',
    // Navigate into the first dataset after load
    action: async (page) => {
      const link = await page.$('a[href*="/datasets/"]');
      if (link) { await link.click(); await page.waitForLoadState('networkidle'); }
    },
    clip: null
  },
  {
    name: '04_scorers_templates',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/scorers`,
    wait: 'networkidle',
    desc: 'Scorers page — template list',
    clip: null
  },
  {
    name: '05_prompts_list',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/prompts`,
    wait: 'networkidle',
    desc: 'Prompts page — New Prompt button',
    clip: null
  },
  {
    name: '06_prompt_editor',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/prompts`,
    wait: 'networkidle',
    desc: 'Prompt editor — system message, {{input}}, slug field',
    action: async (page) => {
      // Click into prompt-a
      const link = await page.$('a[href*="/prompts/prompt-a"], a[href*="/prompts/"]:first-of-type');
      if (link) { await link.click(); await page.waitForLoadState('networkidle'); }
    },
    clip: null
  },
  {
    name: '07_prompt_params_model',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/prompts`,
    wait: 'networkidle',
    desc: 'Prompt Params panel — model selector',
    action: async (page) => {
      const link = await page.$('a[href*="/prompts/"]:first-of-type');
      if (link) {
        await link.click();
        await page.waitForLoadState('networkidle');
        const paramsBtn = await page.$('button:has-text("Params")');
        if (paramsBtn) { await paramsBtn.click(); await page.waitForTimeout(500); }
      }
    },
    clip: null
  },
  {
    name: '08_experiments_form',
    url: `https://www.braintrust.dev/app/${ORG}/p/${PROJECT}/experiments`,
    wait: 'networkidle',
    desc: 'Experiments empty-state setup form',
    clip: null
  },
];

async function run() {
  console.log('\n📸 Braintrust Screenshot Capture\n');
  console.log('A browser window will open. Log in to Braintrust, then come back here.');
  console.log('Screenshots will save automatically to:', OUTPUT_DIR, '\n');

  const browser = await chromium.launch({ headless: false, slowMo: 200 });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  // Navigate to login and wait for the user to authenticate
  await page.goto('https://www.braintrust.dev/app', { waitUntil: 'networkidle' });

  // Wait until we land on the app (not the login/marketing page)
  console.log('⏳ Waiting for you to log in...');
  await page.waitForURL(/\/app\/\w+/, { timeout: 120000 });
  console.log('✅ Logged in! Starting screenshot capture...\n');

  for (const spec of PAGES) {
    console.log(`📷 Capturing: ${spec.desc}`);
    await page.goto(spec.url, { waitUntil: spec.wait || 'networkidle', timeout: 30000 });
    await page.waitForTimeout(800);  // let animations settle

    if (spec.action) {
      await spec.action(page);
      await page.waitForTimeout(600);
    }

    const outPath = path.join(OUTPUT_DIR, `${spec.name}.png`);
    await page.screenshot({
      path: outPath,
      fullPage: false,
      clip: spec.clip || undefined
    });
    console.log(`   ✓ Saved: ${spec.name}.png`);
  }

  await browser.close();
  console.log('\n✅ All done! Screenshots saved to:', OUTPUT_DIR);
  console.log('Now re-run the activity Markdown update to embed the images.\n');
}

run().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
