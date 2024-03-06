<script>
    import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from 'flowbite-svelte';
</script>
  
  <Footer class="fixed inset-x-0 bottom-0 bg-white px-5 py-1">
    <FooterCopyright href="/" by="rodrq" year={2024} />
    <FooterLinkGroup ulClass="flex flex-wrap items-center mt-3 text-sm text-gray-500 dark:text-gray-400 sm:mt-0">
      <FooterLink href="https://github.com/rodrq" target="_blank">Github</FooterLink>
      <FooterLink href="https://www.linkedin.com/in/rodrigo-rooney/" target="_blank">Linkedin</FooterLink>
      <FooterLink href="/contact" target="_blank">Contact</FooterLink>
    </FooterLinkGroup>
  </Footer>