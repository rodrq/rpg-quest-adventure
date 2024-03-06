<script>
	  import { goto } from '$app/navigation';
	  import { toast } from 'svelte-french-toast';
    import emailjs from '@emailjs/browser';


    const sendEmail = (e) => {
      emailjs
        .sendForm(
            import.meta.env.VITE_EMAIL_SERVICE_ID,
            import.meta.env.VITE_EMAIL_TEMPLATE_ID, 
            e.target, {
                publicKey: import.meta.env.VITE_EMAIL_PUBLIC_KEY
        })
        .then(
          () => {
            toast.success("Email sent");
            goto("/")
          },
          (error) => {
            toast.error("Something failed:, ", error.text);
          },
        );
    };
</script>

<head>
  <title>RPG Quest - Contact</title>
</head>

<div class="container mx-auto px-10 py-5 text-gray-600 text-xl ">
  <h1 class="font-bold">Contact me via email. I will respond as soon as I can.</h1>
  <form on:submit|preventDefault={sendEmail} class="max-w-md mx-auto mt-8 p-6 bg-gray-100 rounded-md shadow-md">

    <label for="username" class="block text-gray-700 font-semibold mb-2">Name</label>
    <input type="text" name="username" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500">

    <label for="user_email" class="block mt-4 text-gray-700 font-semibold mb-2">Your email</label>
    <input type="email" name="user_email" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500">

    <label for="message" class="block mt-4 text-gray-700 font-semibold mb-2">Message</label>
    <textarea name="message" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500"></textarea>

    <input type="submit" value="Send" class="mt-4 bg-blue-500 text-white py-2 px-4 rounded-md cursor-pointer hover:bg-blue-600">
  </form>
</div>