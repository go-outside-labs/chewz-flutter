/**
 * GET /
 * Home page.
 */
exports.index = (req, res) => {
  res.render('home', {
    title: 'Chewz',
    bodyClass:'homepage'
  });
};

/**
 * GET /chewzapp
 * Chewz App page.
 */
exports.chewzapp = (req, res) => {
  res.render('chewzapp', {
    title: 'Chewz App',
    bodyClass:'left-sidebar'
  });
};

/**
- * GET /chewzapi
- * Chewz API page.
- */
exports.chewzapi = (req, res) => {
  res.render('chewzapi', {
  title: 'Chewz API'
    });
  };

/**
 * GET /contact
 * Contact page.
 */
exports.contact = (req, res) => {
  res.render('contact', {
    title: 'Contact Us'
  });
};

/**
 * GET /about
 * About page.
 */
exports.about = (req, res) => {
  res.render('about', {
    title: 'About'
  });
};