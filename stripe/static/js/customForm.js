$(function() {
  Stripe.setPublisherKey('pk_test_tzhcDEd89iR85iwQC0qlDQUo');
  let $form = $('#payment-form');

  $form.submit((event) => {
    $form.find('.submit').prop('disabled', true);

    Stripe.card.createToken($form, stripeResponseHandler);

    return false;
  });

  function stripeResponseHandler(status, response) {
    let $form = $('#payment-form');

    if (response.error) {
      $form.find('.payment-errors').text(response.error.message);
      $form.find('.submit').prop('disabled', false);
    } else {
      let token = response.id;

      let input = `
        <input type="hidden" name="stripeToken">
      `;

      $form.append(
        $(input).val(token)
      );

      $form.get(0).submit();
    }
  }
});