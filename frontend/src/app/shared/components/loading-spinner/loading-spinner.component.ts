import { Component, input } from '@angular/core';

@Component({
  selector: 'app-loading-spinner',
  template: `<span class="spinner" [class]="'spinner--' + size()" aria-label="Loading..."></span>`,
  styleUrl: './loading-spinner.component.scss',
})
export class LoadingSpinnerComponent {
  size = input<'sm' | 'md' | 'lg'>('md');
}
