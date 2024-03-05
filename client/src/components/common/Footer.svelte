<script>
    import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from 'flowbite-svelte';
</script>
  
  <Footer class="fixed inset-x-0 bottom-0 bg-white px-5 py-1">
    <FooterCopyright href="/" by="rodrq" year={2024} />
    <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
      <FooterLink href="/">Github</FooterLink>
      <FooterLink href="/">Linkedin</FooterLink>
      <FooterLink href="/">Contact</FooterLink>
    </FooterLinkGroup>
  </Footer>